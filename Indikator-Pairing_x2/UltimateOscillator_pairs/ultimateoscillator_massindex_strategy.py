import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und MassIndex
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'MassIndex': 1.0
        })
    )
