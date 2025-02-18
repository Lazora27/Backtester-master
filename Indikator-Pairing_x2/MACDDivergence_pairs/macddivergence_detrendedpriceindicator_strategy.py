import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DetrendedPriceIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DetrendedPriceIndicator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DetrendedPriceIndicator': 1.0
        })
    )
