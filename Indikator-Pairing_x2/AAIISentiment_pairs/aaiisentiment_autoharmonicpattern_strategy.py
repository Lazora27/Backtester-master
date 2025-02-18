import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
