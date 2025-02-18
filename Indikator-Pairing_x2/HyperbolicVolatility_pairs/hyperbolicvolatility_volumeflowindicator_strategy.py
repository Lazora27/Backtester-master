import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HyperbolicVolatility_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HyperbolicVolatility und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'HyperbolicVolatility': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
