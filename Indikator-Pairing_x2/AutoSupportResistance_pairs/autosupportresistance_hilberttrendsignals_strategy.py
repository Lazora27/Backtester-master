import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
