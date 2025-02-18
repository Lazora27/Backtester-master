import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ProjectionOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
