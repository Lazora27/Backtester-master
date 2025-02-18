import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'AverageTrueRange': 1.0
        })
    )
