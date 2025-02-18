import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
