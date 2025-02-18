import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
