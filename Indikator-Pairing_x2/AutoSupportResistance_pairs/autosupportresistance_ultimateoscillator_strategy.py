import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'UltimateOscillator': 1.0
        })
    )
