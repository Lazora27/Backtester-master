import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DemandIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
