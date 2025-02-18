import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
