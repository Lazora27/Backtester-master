import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
