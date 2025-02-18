import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
