import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'BradleySiderograph': 1.0
        })
    )
