import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
