import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'FlowOfFunds': 1.0
        })
    )
