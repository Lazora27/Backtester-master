import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'FlowOfFunds': 1.0
        })
    )
