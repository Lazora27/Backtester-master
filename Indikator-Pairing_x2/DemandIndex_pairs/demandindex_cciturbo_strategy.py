import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
