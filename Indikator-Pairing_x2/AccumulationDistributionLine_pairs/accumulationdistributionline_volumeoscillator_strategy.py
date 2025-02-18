import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'VolumeOscillator': 1.0
        })
    )
