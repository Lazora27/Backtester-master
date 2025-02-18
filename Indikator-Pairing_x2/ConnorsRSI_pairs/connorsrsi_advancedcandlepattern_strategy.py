import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
