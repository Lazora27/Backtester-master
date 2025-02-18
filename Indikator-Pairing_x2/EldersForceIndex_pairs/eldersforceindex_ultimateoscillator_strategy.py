import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'UltimateOscillator': 1.0
        })
    )
