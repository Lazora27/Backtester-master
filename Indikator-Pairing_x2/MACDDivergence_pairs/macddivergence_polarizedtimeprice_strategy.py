import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
