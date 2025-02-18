import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'KeltnerChannels': 1.0
        })
    )
