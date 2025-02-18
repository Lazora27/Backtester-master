import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'BradleySiderograph': 1.0
        })
    )
