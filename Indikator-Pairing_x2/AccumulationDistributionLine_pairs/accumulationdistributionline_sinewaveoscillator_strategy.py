import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccumulationDistributionLine_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccumulationDistributionLine und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'AccumulationDistributionLine': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
