import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'TimeCycle': 1.0
        })
    )
