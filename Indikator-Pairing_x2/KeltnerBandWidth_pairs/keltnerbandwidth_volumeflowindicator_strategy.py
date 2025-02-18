import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
