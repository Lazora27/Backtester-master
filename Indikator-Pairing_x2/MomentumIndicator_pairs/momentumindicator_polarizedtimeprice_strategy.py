import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
