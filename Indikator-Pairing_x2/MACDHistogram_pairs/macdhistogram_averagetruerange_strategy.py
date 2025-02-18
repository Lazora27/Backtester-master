import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AverageTrueRange': 1.0
        })
    )
