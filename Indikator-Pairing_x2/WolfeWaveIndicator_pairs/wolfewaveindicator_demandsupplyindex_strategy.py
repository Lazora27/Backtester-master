import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
