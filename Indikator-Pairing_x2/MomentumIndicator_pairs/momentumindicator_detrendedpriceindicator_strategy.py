import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_DetrendedPriceIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und DetrendedPriceIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'DetrendedPriceIndicator': 1.0
        })
    )
