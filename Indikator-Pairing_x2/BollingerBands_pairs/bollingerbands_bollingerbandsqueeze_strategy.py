import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
