import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'CCITurbo': 1.0
        })
    )
