import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
