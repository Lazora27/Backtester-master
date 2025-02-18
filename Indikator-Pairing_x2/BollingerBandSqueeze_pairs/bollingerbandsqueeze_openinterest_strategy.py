import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und OpenInterest
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'OpenInterest': 1.0
        })
    )
