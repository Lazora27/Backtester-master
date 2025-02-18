import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'TrendCycles': 1.0
        })
    )
