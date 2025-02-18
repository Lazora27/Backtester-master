import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
