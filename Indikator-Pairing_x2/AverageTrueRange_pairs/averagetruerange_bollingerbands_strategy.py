import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BollingerBands': 1.0
        })
    )
