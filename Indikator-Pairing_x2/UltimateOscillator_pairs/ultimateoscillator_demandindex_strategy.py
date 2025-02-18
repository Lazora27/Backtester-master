import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DemandIndex': 1.0
        })
    )
