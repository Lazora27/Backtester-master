import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'DemandIndex': 1.0
        })
    )
