import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
