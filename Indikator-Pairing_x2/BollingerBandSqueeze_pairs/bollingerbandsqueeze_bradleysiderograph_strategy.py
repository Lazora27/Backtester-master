import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'BradleySiderograph': 1.0
        })
    )
