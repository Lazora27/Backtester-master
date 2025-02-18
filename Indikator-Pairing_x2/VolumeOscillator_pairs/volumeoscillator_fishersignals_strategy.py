import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
