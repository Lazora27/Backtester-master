import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
