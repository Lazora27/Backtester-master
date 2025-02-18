import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'BradleySiderograph': 1.0
        })
    )
