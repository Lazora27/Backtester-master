import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
