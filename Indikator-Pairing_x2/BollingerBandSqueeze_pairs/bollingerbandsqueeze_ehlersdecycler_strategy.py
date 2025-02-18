import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'EhlersDecycler': 1.0
        })
    )
