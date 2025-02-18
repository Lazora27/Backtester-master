import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
