import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ChaikinOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ChaikinOscillator
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ChaikinOscillator': 1.0
        })
    )
