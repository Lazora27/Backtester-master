import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BuyingPressure': 1.0
        })
    )
