import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
