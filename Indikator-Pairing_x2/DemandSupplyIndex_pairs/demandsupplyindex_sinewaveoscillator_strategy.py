import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
