import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'UlcerIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
