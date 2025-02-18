import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
